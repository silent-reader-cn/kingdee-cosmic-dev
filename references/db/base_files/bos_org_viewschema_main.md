# 主数据组织管控范围-bos_org_viewschema_main

## 主数据组织管控范围-多语言表 t_org_viewschema_l

- **表名称：** 主数据组织管控范围-多语言表
- **表名：** t_org_viewschema_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
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

## 主数据组织管控范围-主表 t_org_viewschema

- **表名称：** 主数据组织管控范围-主表
- **表名：** t_org_viewschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | ftreetypeid | 职能类型 | int8 | 64 |  | √ | 0 | [组织职能类型 bos_org_biz](../base_files/bos_org_biz.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcheckerid | fcheckerid | int8 | 64 |  | √ | 0 |  |
| 7 | fbasemaintain | 基础服务维护 | bpchar | 1 |  | √ | '1' | 基础服务维护 |
| 8 | ftreetype | 视图类别 | varchar | 10 |  | √ | '0' | 视图类别 |
| 9 | fusage | fusage | varchar | 10 |  | √ | ' ' |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fcheckdate | fcheckdate | timestamp | 0 |  |  | null |  |
| 19 | fisdefault | 默认 | bpchar | 1 |  | √ | '1' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_org_viewschema_pkey |  | fid |
| 2 | idx_t_org_viewschema_number |  | fnumber,ftreetype |
