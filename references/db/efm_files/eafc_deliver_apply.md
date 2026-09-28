# 移交申请单-eafc_deliver_apply

## 移交目录-子表 tk_eafc_deliver_item

- **表名称：** 移交目录-子表
- **表名：** tk_eafc_deliver_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_volume_num | 案卷数 | int4 | 32 |  | √ | 0 | 案卷数 |
| 3 | fk_eafc_category_no | 类别号 | varchar | 50 |  | √ | ' ' | 类别号 |
| 4 | fk_eafc_category_name | 类别 | varchar | 50 |  | √ | ' ' | 类别 |
| 5 | fk_eafc_file_num | 文件数 | int4 | 32 |  | √ | 0 | 文件数 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fk_eafc_box_address | 实物存放 | varchar | 50 |  | √ | ' ' | 实物存放 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_deliver_item |  | fentryid |

---

## 机构问题-多选基础资料表 tk_eafc_deliver_mul_book

- **表名称：** 机构问题-多选基础资料表
- **表名：** tk_eafc_deliver_mul_book

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_deliver_mul_book |  | fpkid |

---

## 移交申请单-主表 tk_eafc_deliver_apply

- **表名称：** 移交申请单-主表
- **表名：** tk_eafc_deliver_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_org | 申请人部门 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fk_eafc_receiver | 接收系统 | int8 | 64 |  |  | null | [接收方配置 eafc_receiver](../efm_files/eafc_receiver.md) |
| 4 | fk_eafc_dept_select | 选择接收方部门 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fk_eafc_general_archive | 组织机构 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 6 | fk_eafc_auditor | 审批人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fk_eafc_apply_reason | 申请事由 | varchar | 100 |  | √ | ' ' | 申请事由 |
| 9 | fk_eafc_receiver_org_code | 接收方组织编码 | varchar | 50 |  | √ | ' ' | 接收方组织编码 |
| 10 | fk_eafc_description | 移交内容描述 | varchar | 255 |  | √ | ' ' | 移交内容描述 |
| 11 | fcreatorid | 申请人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fk_eafc_org_select | 选择接收方组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 13 | fk_eafc_deliver_mode | 移交方式 | varchar | 50 |  | √ | ' ' | 移交方式,枚举: 1 :在线移交 2 :手动下载 |
| 14 | fk_eafc_contain_entity | 是否包含实物 | varchar | 50 |  | √ | ' ' | 是否包含实物,枚举: 1 :是 2 :否 |
| 15 | fk_eafc_arcorg | 申请人组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 16 | fk_eafc_superintendent | 监交人 | varchar | 50 |  | √ | ' ' | 监交人 |
| 17 | fk_eafc_receiver_phone | 接收人联系方式 | varchar | 30 |  | √ | ' ' | 接收人联系方式 |
| 18 | fk_eafc_audit_result | 审批意见 | varchar | 50 |  | √ | ' ' | 审批意见 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fk_eafc_deliver_user | 移交人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fk_eafc_deliver_phone | 移交人联系方式 | varchar | 30 |  | √ | ' ' | 移交人联系方式 |
| 23 | fk_eafc_receiver_dept | 接收方部门 | varchar | 50 |  | √ | ' ' | 接收方部门 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fk_eafc_start_time | 移交档案开始月份 | timestamp | 0 |  |  | null | 移交档案开始月份 |
| 26 | fk_eafc_recipient_select | 选择接收人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fk_eafc_status | 移交状态 | varchar | 50 |  | √ | ' ' | 移交状态,枚举: 1 :待提交 2 :审批中 3 :已审批 |
| 28 | fk_eafc_billno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 29 | fk_eafc_receiver_org | 接收方组织 | varchar | 50 |  | √ | ' ' | 接收方组织 |
| 30 | fk_eafc_deliver_type | 移交类型 | varchar | 50 |  | √ | ' ' | 移交类型,枚举: 1 :对内移交-综合档案（案卷级） 2 :对内移交-综合档案（文件级） |
| 31 | fk_eafc_recipient | 接收人 | varchar | 50 |  | √ | ' ' | 接收人 |
| 32 | fk_eafc_end_time | 移交档案结束月份 | timestamp | 0 |  |  | null | 移交档案结束月份 |
| 33 | fk_eafc_apply_no | 申请单号 | varchar | 50 |  | √ | ' ' | 申请单号 |
| 34 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_deliver_apply |  | fid |
