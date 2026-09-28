# 渠道分类-ocdbd_channel_class

## 渠道分类-多语言表 t_ocdbd_chl_class_l

- **表名称：** 渠道分类-多语言表
- **表名：** t_ocdbd_chl_class_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_chl_class_l |  | fpkid |
| 2 | idx_ocdbd_chlclassl_flid |  | fid,flocaleid |

---

## 渠道分类-主表 t_ocdbd_chl_class

- **表名称：** 渠道分类-主表
- **表名：** t_ocdbd_chl_class

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | feasnumber | feasnumber | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 5 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 6 | fparentid | 上级分类 | int8 | 64 |  | √ | 0 | 渠道分类 ocdbd_channel_class |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 9 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 10 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 11 | fcustomerclassid | 客户分类主键 | int8 | 64 |  | √ | 0 | 客户分类主键 |
| 12 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 14 | fsalechannelid | 创建渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fclassstype | 分类类型 | bpchar | 1 |  | √ | 'A' | 分类类型,枚举: A :公有分类 B :私有分类 |
| 17 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 19 | fstandardid | 渠道分类标准 | int8 | 64 |  | √ | 0 | 渠道分类标准 ocdbd_channel_standard |
| 20 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_chl_class |  | fid |
| 2 | idx_ocdbd_chlclass_num |  | fnumber |
| 3 | idx_ocdbd_chlclass_parent |  | fparentid |
| 4 | idx_ocdbd_chlclass_salechl |  | fsalechannelid |
