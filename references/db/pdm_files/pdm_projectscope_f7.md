# 项目范围F7（废弃）-pdm_projectscope_f7

## 项目范围F7（废弃）-主表 t_pdm_projscope

- **表名称：** 项目范围F7（废弃）-主表
- **表名：** t_pdm_projscope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fispushtool | 是否下推工具需求 | bpchar | 1 |  | √ | '0' | 是否下推工具需求 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fiscollect | 项目是否在收集范围内 | bpchar | 1 |  | √ | '0' | 项目是否在收集范围内 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcollectmethod | 收集方式 | varchar | 50 |  | √ | ' ' | 收集方式,枚举: A :线上收集 B :线下收集 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | ftoolcreatestatus | 工具需求创建状态 | varchar | 50 |  | √ | ' ' | 工具需求创建状态,枚举: A :未完成 B :已完成 |
| 16 | fispushmat | 是否下推物料需求 | bpchar | 1 |  | √ | '0' | 是否下推物料需求 |
| 17 | fmatcreatestatus | 物料需求创建状态 | varchar | 50 |  | √ | ' ' | 物料需求创建状态,枚举: A :未开始 B :不收集 C :分配中 D :已分配 E :已打印 F :开始收集 G :收集完成 H :取消 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_projscope |  | fid |
| 2 | idx_pdm_projscope_projectid |  | fprojectid |
| 3 | idx_pdm_projscope_billno |  | fbillno |
