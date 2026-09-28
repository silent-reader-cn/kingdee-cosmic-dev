# 批号入库跟踪配置-im_lotintrackconf

## 字段映射-子表 t_im_lotintrackconfentry

- **表名称：** 字段映射-子表
- **表名：** t_im_lotintrackconfentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 3 | finvacccol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_lotintrackconfentry |  | fentryid |
| 2 | idx_im_lottrackcfgentry_id |  | fid |

---

## 批号入库跟踪配置-多语言表 t_im_lotintrackconf_l

- **表名称：** 批号入库跟踪配置-多语言表
- **表名：** t_im_lotintrackconf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_lottrackcfg_l_locale |  | fid,flocaleid |
| 2 | pk_t_im_lotintrackconf_l |  | fpkid |

---

## 批号入库跟踪配置-主表 t_im_lotintrackconf

- **表名称：** 批号入库跟踪配置-主表
- **表名：** t_im_lotintrackconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 6 | fsrcbillobj | 单据 | varchar | 36 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fsrcbillentry | 单据体标识 | varchar | 50 |  | √ | ' ' | 单据体标识 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fbillfilter_tag | 单据过滤条件_详情 | text | 0 |  |  | ' ' | 单据过滤条件_详情 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fbillfilter | 单据过滤条件 | varchar | 255 |  | √ | ' ' | 单据过滤条件 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_lottrackcfg_srcbill |  | fsrcbillobj,fsrcbillentry |
| 2 | pk_t_im_lotintrackconf |  | fid |
| 3 | idx_im_lottrackcfg_number |  | fnumber |
