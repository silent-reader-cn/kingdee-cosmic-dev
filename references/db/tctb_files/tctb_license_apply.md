# 许可授权审批申请单-tctb_license_apply

## 许可授权审批申请单-主表 t_tctb_lic_req

- **表名称：** 许可授权审批申请单-主表
- **表名：** t_tctb_lic_req

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fbillno | 申请编号 | varchar | 30 |  | √ | ' ' | 申请编号 |
| 8 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_licreq_no |  | fbillno |
| 2 | pk_tctb_lic_req |  | fid |

---

## 单据体-子表 t_tctb_lic_req_entry

- **表名称：** 单据体-子表
- **表名：** t_tctb_lic_req_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 许可分组 tctb_license_group |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | flicenseid | licenseid | int8 | 64 |  | √ | 0 | licenseid |
| 5 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fapplystatus | 申请状态 | varchar | 50 |  | √ | ' ' | 申请状态,枚举: A :授权 B :注销 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_lic_req_entry |  | fentryid |
| 2 | idx_tctb_lic_req_entry_fk |  | fid |
