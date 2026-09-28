# 水资源税税源登记信息-tdm_water_source_dj

## 征收子目和税率配置-子表 t_tdm_water_source_entryb

- **表名称：** 征收子目和税率配置-子表
- **表名：** t_tdm_water_source_entryb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 适用税额 | numeric | 23 | 10 | √ | 0 | 适用税额 |
| 3 | fzszm | 征收子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_szys_bizdef_entry |
| 4 | flossrate | 合理损耗率 | numeric | 23 | 10 | √ | 0 | 合理损耗率 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fdecimalfield | fdecimalfield | numeric | 23 | 10 | √ | 0 |  |
| 8 | fdecimalfield1 | fdecimalfield1 | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_water_source_entryb_fk |  | fid |
| 2 | pk_tdm_water_source_entryb |  | fentryid |

---

## 超量用水征收倍数配置-子表 t_tdm_water_source_entry

- **表名称：** 超量用水征收倍数配置-子表
- **表名：** t_tdm_water_source_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcjhbbs2 | 超计划部分征收倍数② | numeric | 23 | 10 | √ | 0 | 超计划部分征收倍数② |
| 3 | fqslcjhbl | 取水量超计划比例（含） | numeric | 23 | 10 | √ | 0 | 取水量超计划比例（含） |
| 4 | fcjhbbs1 | 超计划部分征收倍数① | numeric | 23 | 10 | √ | 0 | 超计划部分征收倍数① |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_water_source_entry |  | fentryid |
| 2 | idx_tdm_water_source_entry_fk |  | fid |

---

## 水资源税税源登记信息-主表 t_tdm_water_source_dj

- **表名称：** 水资源税税源登记信息-主表
- **表名：** t_tdm_water_source_dj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fqyshy | 取用水行业 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_szys_bizdef_entry |
| 4 | fjhnqsl | 计划年取水量 | numeric | 23 | 10 | √ | 0 | 计划年取水量 |
| 5 | fsysedc | 适用税额等次 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_szys_bizdef_entry |
| 6 | fsylx | 水源类型 | varchar | 50 |  | √ | ' ' | 水源类型,枚举: dbs :地表水 dxs :地下水 zls :自来水 |
| 7 | ftsyslb | 特殊用水类别 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_szys_bizdef_entry |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fenddate | 取水许可证有效期止 | timestamp | 0 |  |  | null | 取水许可证有效期止 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fqsdd | 取水地点 | varchar | 50 |  | √ | ' ' | 取水地点 |
| 14 | fqsxkbh | 取水许可证编号 | varchar | 50 |  | √ | ' ' | 取水许可证编号 |
| 15 | fjnqx | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 16 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fqslhdjg | 取水量核定机关 | varchar | 50 |  | √ | ' ' | 取水量核定机关 |
| 21 | fwblqszjs | 未办理取水许可按标准税率倍数计税 | numeric | 23 | 10 | √ | 1 | 未办理取水许可按标准税率倍数计税 |
| 22 | fdxccqlx | 地下超采区类型 | varchar | 50 |  | √ | ' ' | 地下超采区类型,枚举: no :非超采地区 normal :一般超采地区 serious :严重超采地区 |
| 23 | fqsxkzt | 取水许可状态 | varchar | 50 |  | √ | ' ' | 取水许可状态,枚举: 1 :已办理 0 :未办理 |
| 24 | fdxqssffg | 地下取水地点供水管网是否覆盖 | varchar | 50 |  | √ | ' ' | 地下取水地点供水管网是否覆盖,枚举: 1 :是 0 :否 |
| 25 | fstartdate | 取水许可证有效期起 | timestamp | 0 |  |  | null | 取水许可证有效期起 |
| 26 | fsysl | 适用税额 | numeric | 23 | 10 | √ | 0 | 适用税额 |
| 27 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 税源编号 | varchar | 30 |  | √ | ' ' | 税源编号 |
| 29 | fsysbb | 适用申报表 | varchar | 50 |  | √ | ' ' | 适用申报表,枚举: A :水资源税纳税申报表A B :水资源税纳税申报表B |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_water_source_dj |  | fid |
| 2 | idx_tdm_water_source_dj_1 |  | fnumber |

---

## 水资源税税源登记信息-多语言表 t_tdm_water_source_dj_l

- **表名称：** 水资源税税源登记信息-多语言表
- **表名：** t_tdm_water_source_dj_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_water_source_dj_l |  | fpkid |
| 2 | idx_tdm_water_source_dj_l_0 |  | fid,flocaleid |
