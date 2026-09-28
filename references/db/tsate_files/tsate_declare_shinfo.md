# 税号同步信息-tsate_declare_shinfo

## 税号同步信息-主表 t_tsate_declare_shinfo

- **表名称：** 税号同步信息-主表
- **表名：** t_tsate_declare_shinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgtaxnum | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 3 | forgid | 云合同步组织id | varchar | 50 |  | √ | ' ' | 云合同步组织id |
| 4 | forg | 组织 | varchar | 50 |  | √ | ' ' | 组织 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_declare_shinfo |  | fid |
| 2 | idx_tsate_declare_shinfo |  | forgtaxnum |
