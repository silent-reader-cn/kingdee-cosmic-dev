# 组织职能类型-bos_org_biz

## 组织职能类型-多语言表 t_org_bizlist_l

- **表名称：** 组织职能类型-多语言表
- **表名：** t_org_bizlist_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fuserdefinename | 自定义名称 | varchar | 255 |  | √ | ' ' | 自定义名称 |
| 4 | fxkdesc | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_org_bizlist_l_fid |  | fid,flocaleid |
| 2 | t_org_bizlist_l_pkey |  | fpkid |

---

## 组织职能类型-主表 t_org_bizlist

- **表名称：** 组织职能类型-主表
- **表名：** t_org_bizlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fuserdefine | 自定义 | bpchar | 1 |  | √ | ' ' | 自定义 |
| 5 | fcategory | 类别 | varchar | 30 |  | √ | '1' | 类别,枚举: 1 :BU 2 :OT |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fvisiable | 用户可见 | bpchar | 1 |  | √ | '1' | 用户可见 |
| 8 | ffieldname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbasemaintain | 基础服务维护 | bpchar | 1 |  | √ | '1' | 基础服务维护 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :禁用 B :可用 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fisbasetype | 基本职能 | bpchar | 1 |  | √ | ' ' | 基本职能 |
| 17 | fuserdefinename | 自定义名称 | varchar | 255 |  | √ | ' ' | 自定义名称 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fxkdesc | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 20 | fisenabled | 自定义的使用状态 | bpchar | 1 |  | √ | ' ' | 自定义的使用状态 |
| 21 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 22 | fpropertyname | 属性名称 | varchar | 255 |  | √ | ' ' | 属性名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_org_bizlist_pkey |  | fid |
| 2 | idx_t_org_bizlist_num |  | fnumber |
