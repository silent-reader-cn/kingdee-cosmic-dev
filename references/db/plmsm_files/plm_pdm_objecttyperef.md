# 对象引用关系-plm_pdm_objecttyperef

## 对象引用关系-多语言表 t_plm_pdm_objecttyperef_l

- **表名称：** 对象引用关系-多语言表
- **表名：** t_plm_pdm_objecttyperef_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frefobjentityname | 引用实体名称 | varchar | 399 |  | √ | ' ' | 引用实体名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pdm_objecttyperef_l |  | fpkid |
| 2 | idx_plm_pdm_objecttyperef_l_0 |  | fid,flocaleid |

---

## 对象引用关系-主表 t_plm_pdm_objecttyperef

- **表名称：** 对象引用关系-主表
- **表名：** t_plm_pdm_objecttyperef

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | frefobjentityname | 引用实体名称 | varchar | 255 |  | √ | ' ' | 引用实体名称 |
| 5 | fnotifield | 提示字段 | varchar | 50 |  | √ | ' ' | 提示字段 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fnotimessage | 提示信息 | varchar | 255 |  | √ | ' ' | 提示信息 |
| 8 | fobjentitytable | 当前实体表 | varchar | 50 |  | √ | ' ' | 当前实体表 |
| 9 | freftablerout | 引用实体表路由 | varchar | 50 |  | √ | ' ' | 引用实体表路由 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | frefobjentityid | 引用实体编码 | varchar | 50 |  | √ | ' ' | 引用实体编码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | freffieldname | 引用字段 | varchar | 50 |  | √ | ' ' | 引用字段 |
| 15 | fobjmodelid | 当前实体模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 16 | freftablename | 引用实体表 | varchar | 50 |  | √ | ' ' | 引用实体表 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pdm_objecttyperef |  | fid |
| 2 | idx_plm_pdm_objecttyperef_m0 |  | fbillno |
