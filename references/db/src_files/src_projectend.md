# 项目终止&#x2f;废标-src_projectend

## 项目终止&#x2f;废标-主表 t_src_projectend

- **表名称：** 项目终止&#x2f;废标-主表
- **表名：** t_src_projectend

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbiztype | 处理类型 | bpchar | 1 |  | √ | ' ' | 处理类型,枚举: D :进行终止/流标处理 E :进行废标处理 |
| 3 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | 寻源项目变更F7 src_bidchangef7 |
| 4 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 5 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 8 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 10 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_projectend |  | fid |
| 2 | idx_src_projectend_fparentid |  | fparentid |
