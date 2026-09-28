# 条码扫描模型插件管理-barcm_scanmodelplugin

## 条码扫描模型插件管理-多语言表 t_barcm_scmodelplugin_l

- **表名称：** 条码扫描模型插件管理-多语言表
- **表名：** t_barcm_scmodelplugin_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fplugindescription | 插件说明 | varchar | 512 |  | √ | ' ' | 插件说明 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_scmodpgin_fidflid |  | fid,flocaleid |
| 2 | pk_barcm_scmodelplugin_l |  | fpkid |

---

## 条码扫描模型插件管理-主表 t_barcm_scmodelplugin

- **表名称：** 条码扫描模型插件管理-主表
- **表名：** t_barcm_scmodelplugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fpluginpath | 插件路径 | varchar | 255 |  | √ | ' ' | 插件路径 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fplugindescription | 插件说明 | varchar | 512 |  | √ | ' ' | 插件说明 |
| 7 | fispluginpreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 8 | ftargetbillid | 目标单 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fplugintype | 插件类型 | bpchar | 1 |  | √ | ' ' | 插件类型,枚举: A :扫描录入插件 B :源单列表插件 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcebillid | 源单 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_scmodpgin_num |  | fnumber |
| 2 | pk_barcm_scmodelplugin |  | fid |
