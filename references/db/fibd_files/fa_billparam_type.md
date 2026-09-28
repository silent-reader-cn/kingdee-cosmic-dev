# 业务参数类型-fa_billparam_type

## 业务参数类型-主表 t_fa_billparam_type

- **表名称：** 业务参数类型-主表
- **表名：** t_fa_billparam_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fparamrange | 数据取值范围 | varchar | 1000 |  | √ | ' ' | 数据取值范围 |
| 4 | fdefaultval | 默认值 | varchar | 50 |  | √ | ' ' | 默认值 |
| 5 | fbizcloudid | 业务云 | varchar | 36 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 6 | fservicename | 服务名称 | varchar | 50 |  | √ | ' ' | 服务名称 |
| 7 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | fdescription | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 9 | fvaluetype | 参数值类型 | varchar | 20 |  | √ | ' ' | 参数值类型,枚举: password :密码 text :文本 combox :下拉框 long :整数 date :日期 decimal :小数 boolean :开关 |
| 10 | fbizappid | 业务系统 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_billparam_type |  | fid |
| 2 | idx_fa_billparam_type |  | fbizcloudid,fbizappid |
