# 项目终止与重新招标-src_projectend

## 项目终止与重新招标-主表 t_src_projectend

- **表名称：** 项目终止与重新招标-主表
- **表名：** t_src_projectend

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 7 | fnewprojectid | 新招标项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 8 | fsrctypeid | 新招标流程 | int8 | 64 |  | √ | 0 | [寻源流程 pbd_sourceflow](../pbd_files/pbd_sourceflow.md) |
| 9 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 10 | fbiztype | 处理类型 | bpchar | 1 |  | √ | ' ' | 处理类型,枚举: D :进行终止/流标处理 E :进行废标处理 |
| 11 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | [寻源项目变更F7 src_bidchangef7](../pds_files/src_bidchangef7.md) |
| 12 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 13 | fissource | 是否重新招标 | bpchar | 1 |  | √ | '1' | 是否重新招标,枚举: 1 :不需要重新招标 2 :重新招标，复制，创建新项目号 3 :重新招标，复制，项目编号不变 4 :重新招标，不复制，创建新项目号 |
| 14 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fbillno | 新招标项目编号 | varchar | 30 |  | √ | ' ' | 新招标项目编号 |
| 16 | fbidname | 新招标项目名称 | varchar | 300 |  | √ | ' ' | 新招标项目名称 |
| 17 | fversion | 新版本号 | int8 | 64 |  | √ | 1 | 新版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_projectend |  | fid |
| 2 | idx_src_projectend_fparentid |  | fparentid |
