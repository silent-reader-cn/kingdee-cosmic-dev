# 计划版本f7-mpm_planversion_f7

## 计划版本f7-主表 t_mpm_planversion

- **表名称：** 计划版本f7-主表
- **表名：** t_mpm_planversion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fprojectid | 项目编号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 5 | fbillstatus | fbillstatus | varchar | 50 |  | √ | 'C' |  |
| 6 | ftotalplanhours | ftotalplanhours | numeric | 23 | 10 | √ | 0 |  |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fversiontype | 版本类型 | varchar | 50 |  | √ | ' ' | 版本类型,枚举: baseline :基线版本 common :普通版本 |
| 9 | ftotalduration | ftotalduration | numeric | 23 | 10 | √ | 0 |  |
| 10 | fealieststartdate | fealieststartdate | timestamp | 0 |  |  | null |  |
| 11 | flatestenddate | flatestenddate | timestamp | 0 |  |  | null |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillno | 版本号 | varchar | 60 |  | √ | ' ' | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_planversion |  | fid |
| 2 | idx_mpmc_billno_project |  | fbillno,fprojectid |
