# Kbase管理-plm_rengine_kbase

## Kbase管理-主表 t_plm_egn_drlkbase

- **表名称：** Kbase管理-主表
- **表名：** t_plm_egn_drlkbase

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fksessionname | ksession名称 | varchar | 150 |  | √ | ' ' | ksession名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fkbasekey | kbasekey | varchar | 200 |  | √ | ' ' | kbasekey |
| 7 | ftenantid | 租户id | varchar | 100 |  | √ | ' ' | 租户id |
| 8 | fpackagename | 包名称 | varchar | 200 |  | √ | ' ' | 包名称 |
| 9 | fkbasename | kbase名称 | varchar | 150 |  | √ | ' ' | kbase名称 |
| 10 | fkbasenum | kbase编号 | int4 | 32 |  | √ | 0 | kbase编号 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_drlkbase |  | fid |
| 2 | idx_plm_kb_tanantapp |  | ftenantid |
