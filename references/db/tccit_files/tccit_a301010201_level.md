# 高新技术企业相关所属范围底稿-tccit_a301010201_level

## 高新技术企业相关所属范围底稿-主表 t_tccit_a301010201_level

- **表名称：** 高新技术企业相关所属范围底稿-主表
- **表名：** t_tccit_a301010201_level

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fleveltype | 项目 | varchar | 50 |  | √ | ' ' | 项目,枚举: |
| 3 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 5 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 6 | fleveldesc | 内容 | varchar | 50 |  | √ | ' ' | 内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_a301010201_level |  | fid |
| 2 | idx_tccit_a301010201_level |  | forgid,fskssqq,fskssqz,fleveltype |
