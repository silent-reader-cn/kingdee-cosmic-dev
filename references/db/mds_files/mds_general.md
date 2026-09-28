# 通用件自定义清单-mds_general

## 通用件自定义清单-多语言表 t_mds_general_l

- **表名称：** 通用件自定义清单-多语言表
- **表名：** t_mds_general_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_general_l_id |  | fid,flocaleid |
| 2 | pk_mds_general_l |  | fpkid |

---

## 通用件自定义清单-主表 t_mds_general

- **表名称：** 通用件自定义清单-主表
- **表名：** t_mds_general

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_general |  | fid |
| 2 | idx_mds_general_no |  | fnumber |

---

## 单据体-子表 t_mds_generalentity

- **表名称：** 单据体-子表
- **表名：** t_mds_generalentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomer | 客户编码 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 3 | fentrymodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | freasondesc | 原因描述 | varchar | 255 |  | √ | ' ' | 原因描述 |
| 5 | fentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | flongcycle | 长周期 | numeric | 23 | 10 | √ | 0 | 长周期 |
| 7 | favgdelivery | 三年平均交期 | numeric | 23 | 10 | √ | 0 | 三年平均交期 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | factype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 10 | fapplicant | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fentrycreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 13 | fmaterialtype | 物料类型 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 14 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 16 | fislongcyclemater | 是否长周期物料 | bpchar | 1 |  | √ | '0' | 是否长周期物料 |
| 17 | flosedate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_generalentity_id |  | fid |
| 2 | pk_mds_generalentity |  | fentryid |
