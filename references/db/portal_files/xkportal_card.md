# 首页卡片-xkportal_card

## 首页卡片-主表 t_xkbas_card

- **表名称：** 首页卡片-主表
- **表名：** t_xkbas_card

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 卡片名称 | varchar | 80 |  | √ | ' ' | 卡片名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fisshare | 全员共享 | bpchar | 1 |  | √ | '0' | 全员共享 |
| 6 | fappnum | 所属应用（废弃） | varchar | 50 |  | √ | ' ' | 所属应用（废弃） |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fismainpage | 主页应用 | bpchar | 1 |  | √ | '0' | 主页应用 |
| 10 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fconfig | 配置信息 | text | 0 |  |  | ' ' | 配置信息 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | ftype | 卡片类型 | varchar | 36 |  | √ | ' ' | 卡片类型,枚举: |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fisbizapp | 业务应用 | bpchar | 1 |  | √ | '0' | 业务应用 |
| 17 | fnumber | 卡片编码 | varchar | 80 |  | √ | ' ' | 卡片编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbas_card |  | fid |
| 2 | idx_t_xkbas_card_fnumber |  | fnumber |

---

## 所属应用-多选基础资料表 t_xkbas_card_app

- **表名称：** 所属应用-多选基础资料表
- **表名：** t_xkbas_card_app

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_xkbas_card_app_fid |  | fid |
| 2 | pk_t_xkbas_card_app |  | fpkid |

---

## 组织单据体-子表 t_xkbas_card_org

- **表名称：** 组织单据体-子表
- **表名：** t_xkbas_card_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | forgid | 编码 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_xkbas_card_org_fid |  | fid |
| 2 | pk_t_xkbas_card_org |  | fentryid |

---

## 用户单据体-子表 t_xkbas_card_user

- **表名称：** 用户单据体-子表
- **表名：** t_xkbas_card_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fuserid | 编码 | int8 | 64 |  | √ | 0 | [用户信息 bos_usergroup_user](../base_files/bos_usergroup_user.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbas_card_user |  | fentryid |
| 2 | idx_t_xkbas_card_user_fid |  | fid |

---

## 角色单据体-子表 t_xkbas_card_role

- **表名称：** 角色单据体-子表
- **表名：** t_xkbas_card_role

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | froleid | 编码 | varchar | 18 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbas_card_role |  | fentryid |
| 2 | idx_t_xkbas_card_role_fid |  | fid |

---

## 首页卡片-多语言表 t_xkbas_card_l

- **表名称：** 首页卡片-多语言表
- **表名：** t_xkbas_card_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 卡片名称 | varchar | 570 |  | √ | ' ' | 卡片名称 |
| 3 | fcustomname | 自定义名称 | varchar | 500 |  | √ | ' ' | 自定义名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbas_card_l |  | fpkid |
| 2 | idx_t_xkbas_card_l_fid |  | fid |
