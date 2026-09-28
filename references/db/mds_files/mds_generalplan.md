# 通用备货计划-mds_generalplan

## 通用备货计划-主表 t_mds_generalplan

- **表名称：** 通用备货计划-主表
- **表名：** t_mds_generalplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 4 | factualintime | 预计进场时间 | timestamp | 0 |  |  | null | 预计进场时间 |
| 5 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fchecktypedesc | 检修级别名称 | varchar | 50 |  | √ | ' ' | 检修级别名称 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | factype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | frepaircycle | 计划检修周期 | numeric | 23 | 10 | √ | 0 | 计划检修周期 |
| 12 | flogid | 计算日志 | int8 | 64 |  | √ | 0 | 通用备货运算日志 mds_generallog |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fchecktype | 检修级别 | int8 | 64 |  | √ | 0 | 检修级别 mpdm_checktype |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fprojectcreatetime | 项目创建时间 | timestamp | 0 |  |  | null | 项目创建时间 |
| 17 | fproject | 项目编码 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 18 | factualleavetime | 预计离场时间 | timestamp | 0 |  |  | null | 预计离场时间 |
| 19 | fbillno | 计划号 | varchar | 80 |  | √ | ' ' | 计划号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | facreg | 检修设备 | int8 | 64 |  | √ | 0 | 物料 bd_material |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_generalplan |  | fid |
| 2 | idx_mds_generalplan_log |  | flogid |
