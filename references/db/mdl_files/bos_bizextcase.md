# 业务扩展场景-bos_bizextcase

## 业务扩展场景-主表 t_meta_bizextcase

- **表名称：** 业务扩展场景-主表
- **表名：** t_meta_bizextcase

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 业务场景名称 | varchar | 200 |  | √ | ' ' | 业务场景名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | finterfacetype | 扩展接口类型 | bpchar | 1 |  | √ | 'J' | 扩展接口类型,枚举: J :自定义Java接口 E :通用的扩展接口 S :自定义脚本接口 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsample_tag | 插件开发说明_详情 | text | 0 |  |  | null | 插件开发说明_详情 |
| 7 | fisv | 开发商 | varchar | 200 |  | √ | ' ' | 开发商 |
| 8 | finterface | 扩展接口 | varchar | 200 |  | √ | ' ' | 扩展接口 |
| 9 | fbizappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ftssample | ts脚本模板 | varchar | 255 |  | √ | ' ' | ts脚本模板 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsample | 插件开发说明 | varchar | 255 |  | √ | ' ' | 插件开发说明 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fjavasample_tag | java示例_详情 | text | 0 |  |  | null | java示例_详情 |
| 17 | fjavasample | java示例 | varchar | 255 |  | √ | ' ' | java示例 |
| 18 | ftssample_tag | ts脚本模板_详情 | text | 0 |  |  | null | ts脚本模板_详情 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 业务场景编码 | varchar | 200 |  | √ | ' ' | 业务场景编码 |
| 21 | fobjecttype | 所属业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 22 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_bizextcase_num |  | fnumber |
| 2 | pk_meta_bizextcase |  | fid |

---

## 业务扩展场景-多语言表 t_meta_bizextcase_l

- **表名称：** 业务扩展场景-多语言表
- **表名：** t_meta_bizextcase_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 业务场景名称 | varchar | 275 |  | √ | ' ' | 业务场景名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_bizextcase_l_id |  | fid |
| 2 | pk_meta_bizextcase_l |  | fpkid |
