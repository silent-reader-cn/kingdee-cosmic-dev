# 寻源计划项-src_planitem

## 寻源计划项-主表 t_src_planitem

- **表名称：** 寻源计划项-主表
- **表名：** t_src_planitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisv_id | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 3 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbiznodeid | 关联的业务节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 6 | fbizurgeid | 关联的业务催办 | int8 | 64 |  | √ | 0 | 扩展插件 pds_extplugin |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_planitem_fbiznodeid |  | fbiznodeid |
| 2 | idx_src_planitem_fnumber |  | fnumber |
| 3 | idx_src_planitem_fbizurgeid |  | fbizurgeid |
| 4 | pk_src_planitem |  | fid |

---

## 寻源计划项-多语言表 t_src_planitem_l

- **表名称：** 寻源计划项-多语言表
- **表名：** t_src_planitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_planitem_l_fid |  | fid |
| 2 | idx_src_planitem_l_fname |  | fname |
| 3 | pk_src_planitem_l |  | fpkid |
