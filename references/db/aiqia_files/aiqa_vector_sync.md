# 多模态向量同步-aiqa_vector_sync

## 多模态向量同步-多语言表 t_aiqa_vector_sync_l

- **表名称：** 多模态向量同步-多语言表
- **表名：** t_aiqa_vector_sync_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvectorname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | fbrand | 品牌 | varchar | 80 |  | √ | ' ' | 品牌 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aiqa_vector_sync_l |  | fpkid |
| 2 | idx_aiqa_vector_sync_l_0 |  | fid,flocaleid |

---

## 多模态向量同步-主表 t_aiqa_vector_sync

- **表名称：** 多模态向量同步-主表
- **表名：** t_aiqa_vector_sync

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcategory | 品类 | varchar | 200 |  | √ | ' ' | 品类 |
| 4 | fbatchno | 同步批次号 | varchar | 200 |  | √ | ' ' | 同步批次号 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fpictureoverlook | 产品俯视图 | varchar | 255 |  | √ | ' ' | 产品俯视图 |
| 8 | fbrand | 品牌 | varchar | 50 |  | √ | ' ' | 品牌 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fpictureplane | 产品平面图 | varchar | 255 |  | √ | ' ' | 产品平面图 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fvectorname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 15 | fsyncstatus | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: 0 :未同步 1 :已同步 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aiqa_vector_sync_m0 |  | fbillno |
| 2 | pk_aiqa_vector_sync |  | fid |
