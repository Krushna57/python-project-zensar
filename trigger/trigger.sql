-- we can create python module to create this triggers on the database but it is more efficient if we directly apply them on the database
--after insert trigger on the feedback table ***********************************
CREATE OR REPLACE TRIGGER feedback_insert_trigger
AFTER INSERT ON Feedback
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (customer_id, action_type, action_timestamp, modified_by, old_value, new_value)
    VALUES (
        :new.customer_id,               
        'INSERT',                       
        SYSDATE,                         
        'admin',                         
        NULL,                            
        'New Feedback: ' || :new.rating || ' - ' || :new.comments 
    );
END;

--before update trigger on the feedback table 

CREATE OR REPLACE TRIGGER feedback_update_trigger
BEFORE UPDATE ON Feedback
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (customer_id, action_type, action_timestamp, modified_by, old_value, new_value)
    VALUES (
        :new.customer_id,                
        'UPDATE',                        
        SYSDATE,                        
        'admin',                         
        'Old Feedback: ' || :old.rating || ' - ' || :old.comments, 
        'Updated Feedback: ' || :new.rating || ' - ' || :new.comments 
    );
END;

update feedback set rating=3 where feedback_id = 1;
select * from feedback;

--BEFORE delete trigger on the feedback table
CREATE OR REPLACE TRIGGER feedback_delete_trigger
BEFORE DELETE ON Feedback
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (customer_id, action_type, action_timestamp, modified_by, old_value, new_value)
    VALUES (
        :OLD.customer_id,               
        'DELETE',                       
        SYSDATE,                         
        'admin',                        
        'Deleted Feedback: ' || :OLD.rating || ' - ' || :OLD.comments, 
        NULL                             
    );
END;