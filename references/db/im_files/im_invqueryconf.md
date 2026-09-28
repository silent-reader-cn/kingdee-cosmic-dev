# 库存查询配置-im_invqueryconf

## 库存查询字段映射-子表 t_im_invquerymapping

- **表名称：** 库存查询字段映射-子表
- **表名：** t_im_invquerymapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqfilter | 查询条件 | bpchar | 1 |  | √ | '0' | 查询条件 |
| 3 | fmatch | 返回匹配 | bpchar | 1 |  | √ | '0' | 返回匹配 |
| 4 | fsrcbillcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | freturnorder | 返回顺序 | int8 | 64 |  | √ | 0 | 返回顺序 |
| 7 | finvacccolno | finvacccolno | varchar | 100 |  | √ | ' ' |  |
| 8 | ffristout | 优先出库 | bpchar | 1 |  |  | '0' | 优先出库 |
| 9 | fmappingispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 10 | fupdate | 返回单据 | bpchar | 1 |  | √ | '0' | 返回单据 |
| 11 | finvacccol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 12 | ffieldmustinput | 单据字段必录校验 | bpchar | 1 |  |  | '0' | 单据字段必录校验 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fsrcbillcolno | fsrcbillcolno | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_invquerymapping |  | fentryid |
| 2 | idx_im_invqrymap_id |  | fid |

---

## 库存查询配置-多语言表 t_im_invqueryconf_l

- **表名称：** 库存查询配置-多语言表
- **表名：** t_im_invqueryconf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
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
| 1 | idx_im_invqry_l_flid |  | fid,flocaleid |
| 2 | pk_t_im_invqueryconf_l |  | fpkid |

---

## 库存查询配置-主表 t_im_invqueryconf

- **表名称：** 库存查询配置-主表
- **表名：** t_im_invqueryconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcbillobj | 单据 | varchar | 36 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 3 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | foperatekey | 操作代码 | varchar | 50 |  | √ | ' ' | 操作代码 |
| 9 | fnewdeal | 当返回条件不满足时新增单据行 | bpchar | 1 |  | √ | '1' | 当返回条件不满足时新增单据行 |
| 10 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmiddleinsert | 新增单据行时添加至指定行之后 | bpchar | 1 |  | √ | '0' | 新增单据行时添加至指定行之后 |
| 13 | fqtyrule | 返回数量规则 | varchar | 50 |  | √ | ' ' | 返回数量规则,枚举: proqty :供给数量 reqqty :需求数量 minrule :孰小原则 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 16 | fentrynoupdatefieldkey | 不更新库存字段标识 | varchar | 50 |  | √ | ' ' | 不更新库存字段标识 |
| 17 | fusetype | 适用范围 | bpchar | 1 |  |  | 'A' | 适用范围,枚举: A :库存查询 B :出库规则 |
| 18 | fsrcbillentry | 单据体标识 | varchar | 50 |  | √ | ' ' | 单据体标识 |
| 19 | freturntype | 返回值 | varchar | 50 |  | √ | ' ' | 返回值,枚举: null :不返回 single :单行 multi :多行 |
| 20 | fdealtype | 返回值处理方式 | varchar | 50 |  | √ | ' ' | 返回值处理方式,枚举: systemdeal :系统处理 plugindeal :插件处理 |
| 21 | funittran | 库存单位数量按换算率计算返回 | bpchar | 1 |  | √ | '0' | 库存单位数量按换算率计算返回 |
| 22 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | factionid | 关闭回调参数 | varchar | 50 |  | √ | ' ' | 关闭回调参数 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fsrcbillentryname | fsrcbillentryname | varchar | 100 |  | √ | ' ' |  |
| 26 | fproqtyfield | 供给数量字段(废弃) | varchar | 50 |  | √ | ' ' | 供给数量字段(废弃),枚举: avbqty :可用量 qty :库存量 |
| 27 | fpluginname | 返回处理插件 | varchar | 100 |  | √ | ' ' | 返回处理插件 |
| 28 | ffilterpluginname | 过滤插件 | varchar | 100 |  | √ | ' ' | 过滤插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_invqueryconf |  | fid |
| 2 | idx_im_invqry_number |  | fnumber |
| 3 | idx_im_invqry_srcbill |  | fsrcbillobj,foperatekey |
