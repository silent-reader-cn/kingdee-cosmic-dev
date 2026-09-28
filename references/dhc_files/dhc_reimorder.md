# 报账工单-dhc_reimorder

## 报账工单-多语言表 t_dhc_reimorder_l

- **表名称：** 报账工单-多语言表
- **表名：** t_dhc_reimorder_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fposition | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dhc_reimorder_l_id |  | fid,flocaleid |
| 2 | pk_t_dhc_reimorder_l |  | fpkid |

---

## 报账工单-主表 t_dhc_reimorder

- **表名称：** 报账工单-主表
- **表名：** t_dhc_reimorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核通过 E :审核不通过 F :废弃 |
| 4 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdept | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | faccountingorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fattachmentnum | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 12 | fimagenumber | 影像编码 | varchar | 50 |  | √ | ' ' | 影像编码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | ftype | 报账业务类型 | int8 | 64 |  | √ | 0 | 报账业务类型 bd_businessitem |
| 15 | fnextauditor | 当前处理人 | varchar | 50 |  | √ | ' ' | 当前处理人 |
| 16 | fbillno | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dhc_reimorder_billno |  | fbillno |
| 2 | t_dhc_reimorder_pkey |  | fid |
