# 消息通知单-fpy_message_notice

## 单据体-子表 tk_fpy_msg_notice_item

- **表名称：** 单据体-子表
- **表名：** tk_fpy_msg_notice_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fk_fpy_phone | 手机号码 | varchar | 30 |  | √ | ' ' | 手机号码 |
| 4 | fk_fpy_remark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 5 | fk_fpy_recipient | 接收人 | varchar | 50 |  | √ | ' ' | 接收人 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fk_fpy_recipient_select | 接收人选择 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fk_fpy_email | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 9 | fk_eafc_borrowdept | 部门 | varchar | 50 |  | √ | ' ' | 部门 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fk_fpy_login_pass | 提取密钥 | varchar | 50 |  | √ | ' ' | 提取密钥 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_msg_notice_item |  | fentryid |

---

## 消息通知单-主表 tk_fpy_message_notice

- **表名称：** 消息通知单-主表
- **表名：** tk_fpy_message_notice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_fpy_related_id | 关联单据id | int8 | 64 |  | √ | 0 | 关联单据id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 1 :未发送 2 :发送成功 3 :发送失败 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fk_fpy_notice_type | 通知类型 | varchar | 50 |  | √ | ' ' | 通知类型,枚举: 1 :库房移交 2 :档案盘点 3 :其他 4 :档案借阅 5 :档案鉴定 6 :档案销毁 7 :档案移交 |
| 7 | fk_fpy_notice_content | 通知内容 | varchar | 2000 |  | √ | ' ' | 通知内容 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fk_fpy_notice_channel | 通知渠道 | varchar | 50 |  | √ | ' ' | 通知渠道,枚举: 1 :邮件 2 :消息提醒 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fk_fpy_notice_title | 通知标题 | varchar | 200 |  | √ | ' ' | 通知标题 |
| 13 | fk_fpy_apply_no | 申请单号 | varchar | 50 |  | √ | ' ' | 申请单号 |
| 14 | fk_fpy_isborrowlimit | 借阅访问控制 | bpchar | 1 |  | √ | '0' | 借阅访问控制 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_message_notice |  | fid |
