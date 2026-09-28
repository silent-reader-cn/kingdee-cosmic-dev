# 移动首页功能-mpdm_functionconfig

## 移动首页功能-多语言表 t_mpdm_fctionconfig_l

- **表名称：** 移动首页功能-多语言表
- **表名：** t_mpdm_fctionconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_fction_l_fidflid |  | fid,flocaleid |
| 2 | pk_mpdm_fctionconfig_l |  | fpkid |

---

## 移动首页功能-主表 t_mpdm_fctionconfig

- **表名称：** 移动首页功能-主表
- **表名：** t_mpdm_fctionconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [移动功能分组 mpdm_homefuncgroups](../mpdm_files/mpdm_homefuncgroups.md) |
| 6 | fmobopenwith | 打开方式 | bpchar | 1 |  | √ | ' ' | 打开方式,枚举: A :移动表单 B :移动单据 C :移动列表 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fopenparam | 打开参数 | varchar | 255 |  | √ | ' ' | 打开参数 |
| 9 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ficonpath | 图标路径 | varchar | 1000 |  | √ | ' ' | 图标路径 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fbizobjectid | 对应业务对象 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 14 | fseqnumber | 默认顺序号 | int8 | 64 |  | √ | 0 | 默认顺序号 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | ffunctype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: A :移动条码 B :通用 |
| 18 | fmobilebizobjid | 移动页面 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 21 | fscanmodelid | 条码扫描模型 | int8 | 64 |  | √ | 0 | [条码扫描模型 barcm_scanningmodel](../barcm_files/barcm_scanningmodel.md) |
| 22 | fhomepageschemeid | 所属首页方案 | int8 | 64 |  | √ | 0 | [移动首页方案 mpdm_hpschemeconfig](../mpdm_files/mpdm_hpschemeconfig.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_fctionconfig |  | fid |
| 2 | idx_mpdm_fction_number |  | fnumber |
