# 生产领料申请变更字段配置-im_mdc_xmftreqconfig

## 生产领料申请变更字段配置-多语言表 t_im_mdc_xmftreqconfig_l

- **表名称：** 生产领料申请变更字段配置-多语言表
- **表名：** t_im_mdc_xmftreqconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_xmftreqconfig_l |  | fpkid |
| 2 | idx_im_mdc_xmftreqconfig_fid |  | fid,flocaleid |

---

## 生产领料申请变更字段配置-主表 t_im_mdc_xmftreqconfig

- **表名称：** 生产领料申请变更字段配置-主表
- **表名：** t_im_mdc_xmftreqconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mdc_xmftreqconfig_fnumber |  | fnumber |
| 2 | pk_im_mdc_xmftreqconfig |  | fid |

---

## 单据体-子表 t_im_mdc_xmrcentry

- **表名称：** 单据体-子表
- **表名：** t_im_mdc_xmrcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fpropertytype | 字段属性 | varchar | 50 |  | √ | ' ' | 字段属性,枚举: A :单据头 B :单据体 |
| 4 | fpropertyid | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fpropertyname | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_xmrcentry |  | fentryid |
| 2 | idx_mdc_xmrcentry_fid |  | fid |
