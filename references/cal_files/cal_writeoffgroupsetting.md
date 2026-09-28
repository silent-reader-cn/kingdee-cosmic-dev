# 勾稽成组关系配置-cal_writeoffgroupsetting

## 勾稽成组关系配置-多语言表 t_cal_wgroupsetting_l

- **表名称：** 勾稽成组关系配置-多语言表
- **表名：** t_cal_wgroupsetting_l

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
| 1 | pk_cal_wgroupsetting_l |  | fpkid |
| 2 | idx_cal_wgroupsetting_l_id |  | fid |

---

## 源单类型-多选基础资料表 t_cal_wgs_srcbilltype

- **表名称：** 源单类型-多选基础资料表
- **表名：** t_cal_wgs_srcbilltype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_wgs_srcbilltype |  | fpkid |
| 2 | idx_cal_wgs_srcbilltype_eid |  | fentryid |

---

## 成组成本子要素-多选基础资料表 t_cal_wgs_subelement

- **表名称：** 成组成本子要素-多选基础资料表
- **表名：** t_cal_wgs_subelement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_wgs_subelement |  | fpkid |
| 2 | idx_cal_wgs_subelement_id |  | fid |

---

## 勾稽成组关系配置-主表 t_cal_wgroupsetting

- **表名称：** 勾稽成组关系配置-主表
- **表名：** t_cal_wgroupsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 5 | fcostcolumn | 成组成本字段 | varchar | 255 |  | √ | ' ' | 成组成本字段,枚举: materialcost :材料成本 processcost :委外费用 fee :采购成本 manufacturecost :制造费用 resource :人工费用 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 10 | fcostfields | 成组子要素ID | varchar | 255 |  | √ | ' ' | 成组子要素ID |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_wgroup_num |  | fnumber |
| 2 | pk_cal_wgroupsetting |  | fid |

---

## 目标单类型-多选基础资料表 t_cal_wgs_destbilltype

- **表名称：** 目标单类型-多选基础资料表
- **表名：** t_cal_wgs_destbilltype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_wgs_destbilltype_eid |  | fentryid |
| 2 | pk_cal_wgs_destbilltype |  | fpkid |

---

## 核销关系单据体-子表 t_cal_wgroupsettingentry

- **表名称：** 核销关系单据体-子表
- **表名：** t_cal_wgroupsettingentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdbilltypeids | 目标单类型ID | varchar | 255 |  | √ | ' ' | 目标单类型ID |
| 3 | fwftypeid | 核销类别 | int8 | 64 |  | √ | 0 | 核销类别 msmod_writeofftype |
| 4 | fwfrecordid | 核销记录实体 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fsbilltypeids | 源单类型ID | varchar | 255 |  | √ | ' ' | 源单类型ID |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_wgroupsettingentry |  | fentryid |
| 2 | idx_cal_wgroupsetentry_wft |  | fwftypeid |

---

## 主字段单据体-子表 t_cal_wgroupsettingmfield

- **表名称：** 主字段单据体-子表
- **表名：** t_cal_wgroupsettingmfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmainfield | 主字段 | varchar | 80 |  | √ | ' ' | 主字段 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fmainfieldname | 主字段名称 | varchar | 80 |  | √ | ' ' | 主字段名称 |
| 6 | fbilltypeid | 单据类型 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_wgroupsetmf_id |  | fid |
| 2 | pk_cal_wgroupsettingmfield |  | fentryid |
