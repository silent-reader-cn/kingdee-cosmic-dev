# 平板首页功能-osr_pad_functionconfig

## 平板首页功能-主表 t_osr_fctionconfig

- **表名称：** 平板首页功能-主表
- **表名：** t_osr_fctionconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [平板功能分组 osr_pad_homefuncgroups](../osr_files/osr_pad_homefuncgroups.md) |
| 5 | fmobopenwith | 打开方式 | varchar | 50 |  | √ | ' ' | 打开方式,枚举: A :表单 B :单据 C :列表 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fhomepagescheme | 所属首页方案 | int8 | 64 |  | √ | 0 | [首页配置方案 osr_hpschemeconfig](../osr_files/osr_hpschemeconfig.md) |
| 8 | fmobilebizobj | 页面 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 9 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ficonpath | 图标路径 | varchar | 1000 |  | √ | ' ' | 图标路径 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fseqnumber | 默认顺序号 | int4 | 32 |  | √ | 0 | 默认顺序号 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | ffunctype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: B :通用 A :平板 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_osr_fctionconfig |  | fid |
| 2 | idx_t_osr_fctionconfig |  | fhomepagescheme |

---

## 平板首页功能-多语言表 t_osr_fctionconfig_l

- **表名称：** 平板首页功能-多语言表
- **表名：** t_osr_fctionconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 240 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_osr_fctionconfig_l |  | fpkid |
| 2 | idx_t_osr_fctionconfig_l |  | fid,flocaleid |
