# 调度灰度配置-sch_graysetting

## 调度灰度配置-主表 t_sch_graysetting

- **表名称：** 调度灰度配置-主表
- **表名：** t_sch_graysetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 4 | fscheduleid | 调度计划 | varchar | 36 |  | √ | ' ' | [调度计划 sch_schedule](../sys_files/sch_schedule.md) |
| 5 | fwholeapp | 包含下级 | bpchar | 1 |  | √ | '0' | 包含下级 |
| 6 | fappnumber | 应用编码 | varchar | 50 |  | √ | ' ' | 应用编码 |
| 7 | fmodifydate | 修改日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改日期 |
| 8 | fgroup | group | varchar | 50 |  | √ | ' ' | group |
| 9 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fenable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 11 | fgrayver | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 12 | fbizappid | 应用（废弃） | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sch_graysetting_schid |  | fscheduleid |
| 2 | pk_t_sch_graysetting |  | fid |
