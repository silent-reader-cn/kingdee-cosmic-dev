# 维护方案-bos_maindatactlproject

## 维护方案-多语言表 t_org_viewschema_l

- **表名称：** 维护方案-多语言表
- **表名：** t_org_viewschema_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_org_viewschema_l |  | fid,flocaleid |
| 2 | t_org_viewschema_l_pkey |  | fpkid |

---

## 维护方案-主表 t_org_viewschema

- **表名称：** 维护方案-主表
- **表名：** t_org_viewschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 4 | ftreetypeid | ftreetypeid | int8 | 64 |  | √ | 0 |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcheckerid | fcheckerid | int8 | 64 |  | √ | 0 |  |
| 7 | fbasemaintain | fbasemaintain | bpchar | 1 |  | √ | '1' |  |
| 8 | ftreetype | 类型 | varchar | 10 |  | √ | '0' | 类型 |
| 9 | fusage | fusage | varchar | 10 |  | √ | ' ' |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fcheckdate | fcheckdate | timestamp | 0 |  |  | null |  |
| 19 | fisdefault | 默认 | bpchar | 1 |  | √ | '1' | 默认,枚举: 0 :否 1 :是 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_org_viewschema_pkey |  | fid |
| 2 | idx_t_org_viewschema_number |  | fnumber,ftreetype |
