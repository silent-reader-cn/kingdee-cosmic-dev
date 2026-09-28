# 商品标签-pmm_prodlabel

## 商品标签-主表 t_mal_prodlabel

- **表名称：** 商品标签-主表
- **表名：** t_mal_prodlabel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 标签名称 | varchar | 255 |  | √ | ' ' | 标签名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [商品标签分类 pmm_prodlabelgroup](../pmm_files/pmm_prodlabelgroup.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 8 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [商城供应商 bd_malsupplier](../basedata_files/bd_malsupplier.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 标签编码 | varchar | 80 |  | √ | ' ' | 标签编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_prodlabe_fnumber |  | fnumber |
| 2 | pk_t_mal_prodlabel |  | fid |

---

## 商品标签-多语言表 t_mal_prodlabel_l

- **表名称：** 商品标签-多语言表
- **表名：** t_mal_prodlabel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 标签名称 | varchar | 255 |  | √ | ' ' | 标签名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_prodlabel_l_fid |  | fid,flocaleid |
| 2 | pk_t_mal_prodlabel_l |  | fpkid |
