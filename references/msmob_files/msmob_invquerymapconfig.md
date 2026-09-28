# 移动库存查询字段映射配置-msmob_invquerymapconfig

## 单据体-子表 t_mob_invqfieldmapentry

- **表名称：** 单据体-子表
- **表名：** t_mob_invqfieldmapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmobentrykey | 分录标识 | varchar | 50 |  | √ | ' ' | 分录标识 |
| 3 | frealbalfieldname | 字段名称 | varchar | 80 |  | √ | ' ' | 字段名称 |
| 4 | finvfilterfieldname | 字段名称 | varchar | 80 |  | √ | ' ' | 字段名称 |
| 5 | frealbalfieldkey | 字段标识 | varchar | 150 |  | √ | ' ' | 字段标识 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fmobfieldkey | 字段标识 | varchar | 150 |  | √ | ' ' | 字段标识 |
| 8 | fmobfieldtype | 字段类型 | varchar | 80 |  | √ | ' ' | 字段类型 |
| 9 | fispreset | 出厂预设 | bpchar | 1 |  | √ | '0' | 出厂预设 |
| 10 | finvfilterfieldtype | 字段类型 | varchar | 80 |  | √ | ' ' | 字段类型 |
| 11 | finvfilterfieldkey | 字段标识 | varchar | 150 |  | √ | ' ' | 字段标识 |
| 12 | fmobfieldname | 字段名称 | varchar | 80 |  | √ | ' ' | 字段名称 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fisfilter | 参与筛选 | bpchar | 1 |  | √ | '0' | 参与筛选 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invqfieldmap_e_frbfkey |  | frealbalfieldkey |
| 2 | idx_invqfieldmap_e_fid |  | fid |
| 3 | pk_mob_invqfieldmapentry |  | fentryid |

---

## 移动库存查询字段映射配置-主表 t_mob_invquerymapconfig

- **表名称：** 移动库存查询字段映射配置-主表
- **表名：** t_mob_invquerymapconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | finvqueryoptype | 库存查询操作类型 | varchar | 50 |  | √ | ' ' | 库存查询操作类型,枚举: |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmobformid | 移动表单 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_minvqmapcfg_fmform_optype |  | fmobformid,finvqueryoptype |
| 2 | pk_mob_invquerymapconfig |  | fid |

---

## 移动库存查询字段映射配置-多语言表 t_mob_invquerymapconfig_l

- **表名称：** 移动库存查询字段映射配置-多语言表
- **表名：** t_mob_invquerymapconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_minvqmapcfg_l_fid_locale |  | fid,flocaleid |
| 2 | pk_mob_invquerymapconfig_l |  | fpkid |
