# 电子凭证类型-evp_elevouchertype

## 字段配置-子表 t_evp_evtentity

- **表名称：** 字段配置-子表
- **表名：** t_evp_evtentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fisvisibleorigin | 原始数据查询 | bpchar | 1 |  | √ | '0' | 原始数据查询 |
| 5 | fgroupname | 分组名称 | varchar | 50 |  | √ | ' ' | 分组名称 |
| 6 | ffieldnumber | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 7 | fgbnumber | 国标字段标识 | varchar | 200 |  | √ | ' ' | 国标字段标识 |
| 8 | ffieldtype | 字段类型 | bpchar | 1 |  | √ | '1' | 字段类型,枚举: 1 :文本 2 :金额 3 :基础资料 4 :复选框 5 :日期 |
| 9 | fisvisibleevp | 电子凭证池是否展示 | bpchar | 1 |  | √ | '0' | 电子凭证池是否展示 |
| 10 | fgbname | 国标字段名称 | varchar | 200 |  | √ | ' ' | 国标字段名称 |
| 11 | fdisplayprop | 显示属性 | bpchar | 1 |  | √ | '2' | 显示属性,枚举: 1 :编码 2 :名称 3 :编码+名称 4 :长编码 5 :长名称 |
| 12 | fissyspreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evp_evtentity |  | fid |
| 2 | pk_t_evp_evtentity |  | fentryid |

---

## 电子凭证类型-多语言表 t_evp_elevouchertype_l

- **表名称：** 电子凭证类型-多语言表
- **表名：** t_evp_elevouchertype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_evp_elevouchertype_l |  | fpkid |
| 2 | idx_evp_elevouchertype_l |  | fid,flocaleid |

---

## 电子凭证类型-主表 t_evp_elevouchertype

- **表名称：** 电子凭证类型-主表
- **表名：** t_evp_elevouchertype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fstatus | fstatus | bpchar | 1 |  | √ | 'C' |  |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fdispseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 10 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 11 | felevchid | 电子凭证标识 | varchar | 50 |  | √ | ' ' | 电子凭证标识 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_evp_elevouchertype |  | fid |
| 2 | idx_evp_elevouchertype |  | fnumber |
