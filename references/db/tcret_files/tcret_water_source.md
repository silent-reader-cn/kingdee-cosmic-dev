# 水资源税基础信息-tcret_water_source

## 水资源税基础信息-主表 t_tcret_water_resource

- **表名称：** 水资源税基础信息-主表
- **表名：** t_tcret_water_resource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqsxkzblqk | 取水许可证办理情况 | varchar | 50 |  | √ | ' ' | 取水许可证办理情况,枚举: 1 :已办理 0 :未办理 |
| 3 | fqskszdxzqhjdxz | 取水口所在地行政区划、街道乡镇 | varchar | 50 |  | √ | ' ' | 取水口所在地行政区划、街道乡镇 |
| 4 | fqskjtdd | 取水口具体地点 | varchar | 50 |  | √ | ' ' | 取水口具体地点 |
| 5 | fqsxkzbh | 取水许可证编号 | varchar | 50 |  | √ | ' ' | 取水许可证编号 |
| 6 | fqyshy | 取用水行业 | int8 | 64 |  | √ | 0 | 业务定义分录_财行税 tpo_szys_bizdef_entr_cxs |
| 7 | fsysedc | 适用税额等次 | int8 | 64 |  | √ | 0 | 业务定义分录_财行税 tpo_szys_bizdef_entr_cxs |
| 8 | fsylx | 水源类型 | varchar | 50 |  | √ | ' ' | 水源类型,枚举: dbs :地表水 dxs :地下水 |
| 9 | fqsxkyxqq | 取水许可有效期起 | timestamp | 0 |  |  | null | 取水许可有效期起 |
| 10 | fsyse | 适用税额 | numeric | 13 | 4 | √ | 0 | 适用税额 |
| 11 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | ftsyslb | 特殊用水类别 | int8 | 64 |  | √ | 0 | 业务定义分录_财行税 tpo_szys_bizdef_entr_cxs |
| 13 | fsyyxqz | 税源有效期止 | timestamp | 0 |  |  | null | 税源有效期止 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fnxkqsl | 年许可取水量（立方米） | numeric | 15 | 2 | √ | 0 | 年许可取水量（立方米） |
| 17 | fqsxkfzjgxzjb | 取水许可发证机关行政级别 | varchar | 50 |  | √ | ' ' | 取水许可发证机关行政级别,枚举: lyj :流域级 sj :省级 dsj :地市级 xqj :县区级 qt :其他 |
| 18 | fsyyxqq | 税源有效期起 | timestamp | 0 |  |  | null | 税源有效期起 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 21 | fjnqx | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 ansb :按年申报 |
| 22 | fsyxxzxrq | 税源信息注销日期 | timestamp | 0 |  |  | null | 税源信息注销日期 |
| 23 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 26 | fqsxkfzjg | 取水许可发证机关 | varchar | 50 |  | √ | ' ' | 取水许可发证机关 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fsfsyszyyzdqhczdq | 是否属于水资源严重短缺和超载地区 | varchar | 50 |  | √ | ' ' | 是否属于水资源严重短缺和超载地区,枚举: 1 :是 0 :否 |
| 29 | fwblqsxkabzslbsjs | 未办理取水许可按标准税率倍数计税 | numeric | 10 | 2 | √ | 0 | 未办理取水许可按标准税率倍数计税 |
| 30 | fnjhqsl | 年计划取水量（立方米） | numeric | 15 | 2 | √ | 0 | 年计划取水量（立方米） |
| 31 | fqsxkyxqz | 取水许可有效期止 | timestamp | 0 |  |  | null | 取水许可有效期止 |
| 32 | fhlshl | 合理损耗率 | numeric | 10 | 2 | √ | 0 | 合理损耗率 |
| 33 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 34 | fnumber | 税源编号 | varchar | 30 |  | √ | ' ' | 税源编号 |
| 35 | fsyxxbgsxrq | 税源信息变更生效日期 | timestamp | 0 |  |  | null | 税源信息变更生效日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_water_resource |  | fid |

---

## 水资源税基础信息-多语言表 t_tcret_water_resource_l

- **表名称：** 水资源税基础信息-多语言表
- **表名：** t_tcret_water_resource_l

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
| 1 | pk_tcret_water_resource_l |  | fpkid |
| 2 | idx_tcret_water_resource_l_0 |  | fid,flocaleid |
