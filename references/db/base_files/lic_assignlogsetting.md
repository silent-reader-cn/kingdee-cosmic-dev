# 许可分配日志配置-lic_assignlogsetting

## 许可分配日志配置-主表 t_lic_assignlogsetting

- **表名称：** 许可分配日志配置-主表
- **表名：** t_lic_assignlogsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fretaindays | 日志保留天数 | int4 | 32 |  | √ | 0 | 日志保留天数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_assignlogsetting |  | fid |
| 2 | ix_lic_assignlogset_retainday |  | fretaindays |
