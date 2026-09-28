# 外派工作登记单-pom_exworkregisorder

## 外派工作登记单-主表 t_pom_exworkregis

- **表名称：** 外派工作登记单-主表
- **表名：** t_pom_exworkregis

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | forderid | 检修工单主ID | int8 | 64 |  | √ | 0 | 检修工单主ID |
| 4 | fmanupersonid | 外派人工号 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_manuperson |
| 5 | forderentryid | 检修工单行ID | int8 | 64 |  | √ | 0 | 检修工单行ID |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | farrivedate | 到达工作地时间 | timestamp | 0 |  |  | null | 到达工作地时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdepartureflight | 出发航班 | varchar | 50 |  | √ | ' ' | 出发航班 |
| 10 | fentryprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 11 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 12 | freturndate | 返回时间 | timestamp | 0 |  |  | null | 返回时间 |
| 13 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | forderseq | 检修工单行号 | varchar | 50 |  | √ | ' ' | 检修工单行号 |
| 16 | fregisdate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fleaveassignedwork | 离开当天被安排工作 | bpchar | 1 |  | √ | ' ' | 离开当天被安排工作 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | forderno | 检修工单编号 | varchar | 50 |  | √ | ' ' | 检修工单编号 |
| 22 | fdeparturedate | 出发时间 | timestamp | 0 |  |  | null | 出发时间 |
| 23 | fleaveworkbasedate | 离开工作地时间 | timestamp | 0 |  |  | null | 离开工作地时间 |
| 24 | fleaveflight | 离开工作地航班 | varchar | 50 |  | √ | ' ' | 离开工作地航班 |
| 25 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | farriveassignedwork | 到达当天被安排工作 | bpchar | 1 |  | √ | ' ' | 到达当天被安排工作 |
| 28 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_exworkregis |  | fid |
| 2 | idx_pom_exworkregis_fbillno |  | fbillno |
| 3 | idx_pom_exworkregis_forgid |  | forgid |

---

## 工作内容-子表 t_pom_exworkregisentry

- **表名称：** 工作内容-子表
- **表名：** t_pom_exworkregisentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fworkdate | 工作日期 | timestamp | 0 |  |  | null | 工作日期 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fworkremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 6 | fworkcontent | 工作内容 | varchar | 50 |  | √ | ' ' | 工作内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_exworkregisentry |  | fentryid |
| 2 | idx_pom_exworkrentry_fidseq |  | fid,fseq |
