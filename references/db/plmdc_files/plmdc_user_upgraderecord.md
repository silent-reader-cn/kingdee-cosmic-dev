# CAD模型用户升级提示记录-plmdc_user_upgraderecord

## CAD模型用户升级提示记录-主表 t_plmdc_upgrade_record

- **表名称：** CAD模型用户升级提示记录-主表
- **表名：** t_plmdc_upgrade_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frecordate | 今日不再提示日期 | timestamp | 0 |  |  | null | 今日不再提示日期 |
| 3 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_upgrade_record |  | fuserid |
| 2 | pk_t_plmdc_upgrade_record |  | fid |
