# 首页方案-gxyportal_scheme

## 首页方案-主表 t_bas_mainpagelayout

- **表名称：** 首页方案-主表
- **表名：** t_bas_mainpagelayout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | flayout | 布局信息 | text | 0 |  |  | null | 布局信息 |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | flayout_tag | 布局信息_详情 | text | 0 |  |  | ' ' | 布局信息_详情 |
| 9 | fformnum | 表单编码 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 10 | fschemetype | 方案类型 | bpchar | 1 |  | √ | '1' | 方案类型,枚举: 1 :全局方案 2 :共享方案 3 :个性方案 |
| 11 | fispreset | 系统预设 | bpchar | 1 |  | √ | '1' | 系统预设 |
| 12 | fismultiorg | 产品类型 | bpchar | 1 |  | √ | '1' | 产品类型,枚举: 1 :金蝶云星瀚 0 :单组织单法人 2 :金蝶云下一代 4 :金蝶云星空 |
| 13 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 14 | fcustomable | 允许个性化 | bpchar | 1 |  | √ | '1' | 允许个性化 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 17 | ftype | 首页类型 | varchar | 36 |  | √ | ' ' | 首页类型,枚举: main :门户首页 app :应用首页 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 22 | fisdef | 默认首页 | bpchar | 1 |  | √ | '0' | 默认首页 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bas_mplayout |  | ftype,fbizappid,fenable,fcreatorid,fschemetype |
| 2 | t_bas_mainpagelayout_pkey |  | fid |
| 3 | idx_t_bas_mplayout_fuserid |  | fuserid |

---

## 首页方案-多语言表 t_bas_mainpagelayout_l

- **表名称：** 首页方案-多语言表
- **表名：** t_bas_mainpagelayout_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_mainpagelayout_l_pkey |  | fpkid |
| 2 | idx_t_bas_mainpagelayout_l |  | fid,flocaleid |
