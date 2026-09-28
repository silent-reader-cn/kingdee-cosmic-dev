# 基础资料引用关系-bos_objecttyperef

## 基础资料引用关系-主表 t_meta_objecttyperef

- **表名称：** 基础资料引用关系-主表
- **表名：** t_meta_objecttyperef

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fassttypeid | 辅助资料分类 | varchar | 36 |  | √ | ' ' | 辅助资料分类 |
| 3 | fsqlloadidbytime | 按日期查询内码 | varchar | 500 |  | √ | ' ' | 按日期查询内码 |
| 4 | ffieldname | 基础资料物理字段 | varchar | 30 |  | √ | ' ' | 基础资料物理字段 |
| 5 | frefobjecttypeid | 基础资料主实体编码 | varchar | 36 |  | √ | ' ' | 基础资料主实体编码 |
| 6 | frefentityid | 基础资料实体内码 | varchar | 36 |  | √ | ' ' | 基础资料实体内码 |
| 7 | ftablename | 单据物理表格 | varchar | 30 |  | √ | ' ' | 单据物理表格 |
| 8 | fentityid | 单据实体内码 | varchar | 36 |  | √ | ' ' | 单据实体内码 |
| 9 | fobjecttypeid | 单据主实体编码 | varchar | 36 |  | √ | ' ' | 单据主实体编码 |
| 10 | ffieldkey | ffieldkey | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_objecttyperef_base |  | frefobjecttypeid |
| 2 | idx_meta_objecttyperef_bill |  | fobjecttypeid |
| 3 | t_meta_objecttyperef_pkey |  | fid |
| 4 | idx_meta_objectref_refeid |  | frefentityid |
| 5 | idx_meta_objectref_entityid |  | fentityid |
