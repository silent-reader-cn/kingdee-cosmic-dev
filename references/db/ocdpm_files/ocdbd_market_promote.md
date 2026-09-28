# 节假日活动海报-ocdbd_market_promote

## 组织范围-多选基础资料表 t_ocdbd_mktpromoteorg

- **表名称：** 组织范围-多选基础资料表
- **表名：** t_ocdbd_mktpromoteorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_mktpromoteorg |  | fpkid |
| 2 | idx_ocdbd_mktpromoteorg_fid |  | fid |

---

## 节假日活动海报-主表 t_ocdbd_mktpromote

- **表名称：** 节假日活动海报-主表
- **表名：** t_ocdbd_mktpromote

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fapprovedate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 4 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 7 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 10 | fsubjectpic | 主题图 | varchar | 255 |  | √ | ' ' | 主题图 |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fdescription | 营销活动海报 | varchar | 255 |  | √ | ' ' | 营销活动海报 |
| 13 | fcontrolmode | 控制方式 | bpchar | 1 |  | √ | '0' | 控制方式,枚举: 0 :适用所有门店 2 :适用指定门店 |
| 14 | fstarttime | 活动开始日期 | timestamp | 0 |  |  | null | 活动开始日期 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fdescription_tag | 营销活动海报_详情 | text | 0 |  |  | null | 营销活动海报_详情 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fendtime | 活动结束日期 | timestamp | 0 |  |  | null | 活动结束日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_mktpromote_num |  | fnumber |
| 2 | pk_ocdbd_mktpromote |  | fid |

---

## 渠道分类-多选基础资料表 t_ocdbd_mktpromotechan

- **表名称：** 渠道分类-多选基础资料表
- **表名：** t_ocdbd_mktpromotechan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_mktpromotechan_id |  | fid |
| 2 | pk_ocdbd_mktpromotechan |  | fpkid |

---

## 节假日活动海报-多语言表 t_ocdbd_mktpromote_l

- **表名称：** 节假日活动海报-多语言表
- **表名：** t_ocdbd_mktpromote_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_mktpromote_l |  | fpkid |
| 2 | idx_ocdbd_mktpromotel_flid |  | fid,flocaleid |

---

## 适用门店范围-子表 t_ocdbd_mktpromotestore

- **表名称：** 适用门店范围-子表
- **表名：** t_ocdbd_mktpromotestore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisapply | 是否适用 | bpchar | 1 |  | √ | '1' | 是否适用 |
| 3 | fbranchid | 门店编码 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 4 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_mktpromotestore_id |  | fid |
| 2 | pk_ocdbd_mktpromotestore |  | fentryid |
