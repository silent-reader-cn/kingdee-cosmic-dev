# 移动端扩展配置-ocdbd_mobextend

## 移动端扩展配置-多语言表 t_ocdbd_mobextend_l

- **表名称：** 移动端扩展配置-多语言表
- **表名：** t_ocdbd_mobextend_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_mobextend |  | fid,flocaleid |
| 2 | pk_ocdbd_mobextend_l |  | fpkid |

---

## 移动端扩展配置-主表 t_ocdbd_mobextend

- **表名称：** 移动端扩展配置-主表
- **表名：** t_ocdbd_mobextend

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fpcentity | PC表单 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmobentity | 移动表单 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 13 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_mobextend_num |  | fnumber |
| 2 | pk_ocdbd_mobextend |  | fid |

---

## 单据体-子表 t_ocdbd_mobext_colmap

- **表名称：** 单据体-子表
- **表名：** t_ocdbd_mobext_colmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmobcol | 移动表单字段标识 | varchar | 100 |  | √ | ' ' | 移动表单字段标识 |
| 3 | fmobcol_name | 移动表单字段名称 | varchar | 100 |  | √ | ' ' | 移动表单字段名称 |
| 4 | fpccol | pc表单字段标识 | varchar | 100 |  | √ | ' ' | pc表单字段标识 |
| 5 | ffullmobcol | 移动表单字段全标识 | varchar | 100 |  | √ | ' ' | 移动表单字段全标识 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fpccol_name | pc表单字段名称 | varchar | 100 |  | √ | ' ' | pc表单字段名称 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | ffullpccol | pc表单字段全标识 | varchar | 100 |  | √ | ' ' | pc表单字段全标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_mobext_colmap |  | fentryid |
| 2 | idx_ocdbd_mobext_colmap |  | fid |
