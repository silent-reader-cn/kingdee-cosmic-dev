# 回头票据设置-cdm_returnnoteset

## 回头票据设置-多语言表 t_cdm_returnnoteset_l

- **表名称：** 回头票据设置-多语言表
- **表名：** t_cdm_returnnoteset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_returnnoteset_l |  | fpkid |
| 2 | idx_cdm_returnnoteset_l |  | fid |

---

## 回头票据设置-主表 t_cdm_returnnoteset

- **表名称：** 回头票据设置-主表
- **表名：** t_cdm_returnnoteset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frejectremark | 拒收备注 | varchar | 255 |  | √ | ' ' | 拒收备注 |
| 3 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 5 | ftransfercotr | 回填票据转让控制 | varchar | 30 |  | √ | ' ' | 回填票据转让控制,枚举: no :不控制 man :人工控制 transfer :控制转让 |
| 6 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 9 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fsignincotr | 回头票据签收逻辑 | varchar | 30 |  | √ | ' ' | 回头票据签收逻辑,枚举: no :不控制 man :人工控制 reject :拒绝签收 |
| 12 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fexcependoriscop | 被背书人类型为公司时例外 | bpchar | 1 |  | √ | '0' | 被背书人类型为公司时例外 |
| 17 | fexcependorsereqendor | 被背书人与背书人相同时例外 | bpchar | 1 |  | √ | '0' | 被背书人与背书人相同时例外 |
| 18 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_returnnoteset |  | fnumber |
| 2 | pk_t_cdm_returnnoteset |  | fid |
