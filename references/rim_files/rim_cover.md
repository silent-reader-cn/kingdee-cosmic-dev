# 封面-rim_cover

## 封面-主表 t_rim_cover

- **表名称：** 封面-主表
- **表名：** t_rim_cover

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcover_no | 封面编号 | varchar | 50 |  | √ | ' ' | 封面编号 |
| 3 | fcover_type | 封面类型 | varchar | 10 |  | √ | ' ' | 封面类型,枚举: 1 :PDF 2 :图片 |
| 4 | fupdate_time | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fcover_url | 封面url | varchar | 150 |  | √ | ' ' | 封面url |
| 7 | fsnapshot_url | 快照地址 | varchar | 150 |  | √ | ' ' | 快照地址 |
| 8 | fresource | 来源 | varchar | 10 |  | √ | ' ' | 来源,枚举: 1 :手工维护 2 :正常提交报销单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_cover |  | fcover_no,fresource |
| 2 | pk_rim_cover |  | fid |
