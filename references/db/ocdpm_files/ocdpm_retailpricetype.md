# 零售价格类型-ocdpm_retailpricetype

## 零售价格类型-多语言表 t_ocdpm_rtpricetype_l

- **表名称：** 零售价格类型-多语言表
- **表名：** t_ocdpm_rtpricetype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 价格类型名称 | varchar | 100 |  | √ | ' ' | 价格类型名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_rtpricetypel_lid |  | fid,flocaleid |
| 2 | pk_ocdpm_rtpricetype_l |  | fpkid |

---

## 零售价格类型-主表 t_ocdpm_rtpricetype

- **表名称：** 零售价格类型-主表
- **表名：** t_ocdpm_rtpricetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 价格类型名称 | varchar | 100 |  | √ | ' ' | 价格类型名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fisallowadjust | 是否允许门店调整 | bpchar | 1 |  | √ | '0' | 是否允许门店调整 |
| 6 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fshortnumber | 助记码 | varchar | 30 |  | √ | ' ' | 助记码 |
| 9 | fapprovetime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fdisablerid | 失效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fiscontrolprice | 是否控价 | bpchar | 1 |  | √ | '0' | 是否控价 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fdisabletime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | flevel | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 16 | fallowadjustnum | 允许调整次数 | int4 | 32 |  | √ | 0 | 允许调整次数 |
| 17 | fpricefield | 对应价目表字段 | bpchar | 1 |  | √ | ' ' | 对应价目表字段,枚举: A :标准零售价 B :厂家控价 C :唯一价 D :会员价 E :特价 F :预留价格1 G :预留价格2 H :预留价格3 I :预留价格4 J :预留价格5 |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :失效 1 :生效 |
| 21 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 22 | fissyspreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 23 | fuseterminal | 适用终端 | bpchar | 1 |  | √ | ' ' | 适用终端,枚举: A :适用线上 B :适用线下 C :线上线下通用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_rtpricetype_num |  | fnumber |
| 2 | pk_ocdpm_rtpricetype |  | fid |
