# 分类对应表-pmm_catmapping

## 分类对应表-主表 t_mal_catmatgroup

- **表名称：** 分类对应表-主表
- **表名：** t_mal_catmatgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcategoryln | 商品分类长编码 | varchar | 50 |  | √ | ' ' | 商品分类长编码 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmaterialgroup | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 5 | fcategory | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 pbd_goodsclass](../pbd_files/pbd_goodsclass.md) |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fbilldate | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 9 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 10 | fmaterialgroupln | 物料分类长编码 | varchar | 50 |  | √ | ' ' | 物料分类长编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mal_catmatgroup |  | fid |
| 2 | idx_mal_catmatgroup |  | fbillno |

---

## 商品分类-多选基础资料表 t_mal_categorys

- **表名称：** 商品分类-多选基础资料表
- **表名：** t_mal_categorys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
