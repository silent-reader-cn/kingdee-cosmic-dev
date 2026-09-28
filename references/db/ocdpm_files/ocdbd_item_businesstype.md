# 商品经营方式-ocdbd_item_businesstype

## 商品经营方式-主表 t_ocdbd_item_biztype

- **表名称：** 商品经营方式-主表
- **表名：** t_ocdbd_item_biztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | fcreator | int8 | 64 |  | √ | 0 |  |
| 3 | fname | fname | bpchar | 100 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifier | fmodifier | int8 | 64 |  | √ | 0 |  |
| 7 | ffmasterid | ffmasterid | int8 | 64 |  | √ | 0 |  |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已保存 C :已提交 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 14 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 ocdbd_biztype |
| 15 | fnumber | 经营方式编码 | varchar | 80 |  | √ | ' ' | 经营方式编码 |
| 16 | fcommoditymode | 经营方式类型 | bpchar | 1 |  | √ | '0' | 经营方式类型,枚举: 0 :经销 1 :代销 2 :流水倒扣 3 :寄售 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_item_biztype |  | fid |
| 2 | idx_ocdbd_itembiztype_num |  | fnumber |

---

## 商品经营方式-多语言表 t_ocdbd_item_biztype_l

- **表名称：** 商品经营方式-多语言表
- **表名：** t_ocdbd_item_biztype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 经营方式名称 | varchar | 100 |  | √ | ' ' | 经营方式名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_item_biztype_l |  | fpkid |
| 2 | idx_ocdbd_ibiztypel_flid |  | fid,flocaleid |
