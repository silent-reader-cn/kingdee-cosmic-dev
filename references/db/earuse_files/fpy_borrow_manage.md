# 借阅管理-fpy_borrow_manage

## 单据体-子表 tk_eafc_borrowmanag_e

- **表名称：** 单据体-子表
- **表名：** tk_eafc_borrowmanag_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_description | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 3 | fk_eafc_borrowphone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 4 | fk_fpy_curlogin_times | 当前访问次数 | int4 | 32 |  | √ | 0 | 当前访问次数 |
| 5 | fk_fpy_login_times | 访问次数 | int4 | 32 |  | √ | 0 | 访问次数 |
| 6 | fk_fpy_login_ip | 访问设备ip | varchar | 200 |  | √ | ' ' | 访问设备ip |
| 7 | fk_eafc_borrowuser | 借阅人 | varchar | 50 |  | √ | ' ' | 借阅人 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fk_eafc_borrowdept | 借阅部门 | varchar | 50 |  | √ | ' ' | 借阅部门 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fk_eafc_borrowemail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 12 | fk_fpy_login_pass | 提取密钥 | varchar | 50 |  | √ | ' ' | 提取密钥 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_borrowmanag_e_01 |  | fid |
| 2 | pk_eafc_borrowmanag_e |  | fentryid |

---

## 借阅管理-主表 tk_fpy_borrow_manage

- **表名称：** 借阅管理-主表
- **表名：** tk_fpy_borrow_manage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_borrow_way_type | 分类 | varchar | 50 |  | √ | ' ' | 分类 |
| 3 | fk_eafc_borrow_count | 借阅数量 | varchar | 50 |  | √ | ' ' | 借阅数量 |
| 4 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fk_eafc_borrow_way | 借阅形式 | varchar | 50 |  | √ | ' ' | 借阅形式,枚举: 1 :按件借阅 2 :按卷借阅 3 :分类借阅 |
| 6 | fk_fpy_return_days | 归还剩余天数 | int4 | 32 |  | √ | 0 | 归还剩余天数 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fk_fpy_notice_status | 通知状态 | varchar | 50 |  | √ | ' ' | 通知状态,枚举: 1 :未通知 2 :已通知 3 :发送失败 |
| 10 | fk_eafc_slippage | 逾期天数 | varchar | 50 |  | √ | ' ' | 逾期天数 |
| 11 | fk_borrow_reason_type | 借阅事由类型 | varchar | 50 |  | √ | ' ' | 借阅事由类型,枚举: 1 :查账需要借阅 2 :历史账务清理 3 :政府项目审计 4 :年度审计 5 :诉讼 6 :客户发票遗失 7 :项目申报 8 :税局抽查 9 :企业上云 10 :其他 |
| 12 | fk_eafc_borrow_type | 是否包含实物 | varchar | 50 |  | √ | ' ' | 是否包含实物,枚举: 1 :否 2 :是 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fk_eafc_borrow_dept | 借阅部门 | varchar | 50 |  | √ | ' ' | 借阅部门 |
| 15 | fk_eafc_arcorg | 申请人组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 16 | fk_eafc_borrow_manuscript | 实物稿本 | varchar | 50 |  | √ | ' ' | 实物稿本,枚举: 1 :原件 2 :打印副本 |
| 17 | fk_eafc_return_date | 归还时间 | timestamp | 0 |  |  | null | 归还时间 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fk_eafc_return_count | 已归还数量 | varchar | 50 |  | √ | ' ' | 已归还数量 |
| 22 | fk_eafc_borrow_reason | 借阅事由 | varchar | 50 |  | √ | ' ' | 借阅事由 |
| 23 | fk_eafc_fid_lists | 借阅清单id | varchar | 1505 |  | √ | ' ' | 借阅清单id |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fk_eafc_start_time | 借阅起始时间.开始 | timestamp | 0 |  |  | null | 借阅起始时间.开始 |
| 26 | fk_eafc_borrow_user | 借阅人 | varchar | 50 |  | √ | ' ' | 借阅人 |
| 27 | fk_eafc_carrier_type | 载体形态 | varchar | 50 |  | √ | ' ' | 载体形态,枚举: 1 :文件 2 :案卷 |
| 28 | fk_eafc_borrow_email | 借阅人邮箱 | varchar | 50 |  | √ | ' ' | 借阅人邮箱 |
| 29 | fk_fpy_recall_status | 催还状态 | varchar | 50 |  | √ | ' ' | 催还状态,枚举: 1 :未催还 2 :已催还 |
| 30 | fk_eafc_borrow_no | 借阅单号 | varchar | 50 |  | √ | ' ' | 借阅单号 |
| 31 | fk_eafc_end_time | 借阅起始时间.结束 | timestamp | 0 |  |  | null | 借阅起始时间.结束 |
| 32 | fk_fpy_isborrowlimit | 借阅访问控制 | bpchar | 1 |  | √ | '0' | 借阅访问控制 |
| 33 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__fpy_borrow_manage |  | fid |
