# 预算维度映射-xkbm_dimmapping

## 预算维度映射-主表 t_xkbm_dimmapping

- **表名称：** 预算维度映射-主表
- **表名：** t_xkbm_dimmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 570 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [预算维度映射分组 xkbm_dimmappinggroup](../xkbm_files/xkbm_dimmappinggroup.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ffunc | 取数函数 | varchar | 20 |  | √ | ' ' | 取数函数,枚举: 0 :Acct |
| 7 | fasstacttype | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 8 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fmuliattributename | 属性字段多语言 | varchar | 570 |  | √ | ' ' | 属性字段多语言 |
| 11 | fmappingrule | 映射规则 | varchar | 10 |  | √ | ' ' | 映射规则,枚举: 0 :自定义匹配 1 :按编码匹配 2 :按名称匹配 3 :维度与属性维度 4 :维度与多层级维度 |
| 12 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fattributekey | 属性字段标识 | varchar | 100 |  | √ | ' ' | 属性字段标识 |
| 16 | fscene | 应用场景 | varchar | 10 |  | √ | ' ' | 应用场景,枚举: 0 :编制维度与控制维度差异 1 :编制维度与取数函数参数差异 |
| 17 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | ffuncargtype | 取数参数类型 | varchar | 20 |  | √ | ' ' | 取数参数类型,枚举: |
| 20 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 21 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_dimmapping |  | fnumber |
| 2 | pk_xkbm_dimmapping |  | fid |

---

## 控制维度-多选基础资料表 t_xkbm_dimmappingctrl

- **表名称：** 控制维度-多选基础资料表
- **表名：** t_xkbm_dimmappingctrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_dimmappingctrl |  | fpkid |
| 2 | idx_xkbm_dimmappingctrl |  | fid |

---

## 编制维度-多选基础资料表 t_xkbm_dimmappingrpt

- **表名称：** 编制维度-多选基础资料表
- **表名：** t_xkbm_dimmappingrpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_dimmappingrpt |  | fid |
| 2 | pk_xkbm_dimmappingrpt |  | fpkid |

---

## 预算维度映射-多语言表 t_xkbm_dimmapping_l

- **表名称：** 预算维度映射-多语言表
- **表名：** t_xkbm_dimmapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 570 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fmuliattributename | 属性字段多语言 | varchar | 570 |  | √ | ' ' | 属性字段多语言 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_dimmapping_l |  | fid,flocaleid |
| 2 | pk_xkbm_dimmapping_l |  | fpkid |

---

## 控制维度字段关系-子表 t_xkbm_ctrldimmapping

- **表名称：** 控制维度字段关系-子表
- **表名：** t_xkbm_ctrldimmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fctrldimcategory | 维度类型 | varchar | 10 |  | √ | ' ' | 维度类型 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fctrlmappingasstacttype | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 5 | fctrlfieldkey | 对应字段 | varchar | 50 |  | √ | ' ' | 对应字段 |
| 6 | fctrldimname | 维度名称 | varchar | 570 |  | √ | ' ' | 维度名称 |
| 7 | fctrldimformid | 页面标识 | varchar | 50 |  | √ | ' ' | 页面标识 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fctrlmappingdimid | 控制维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_ctrldimmapping |  | fentryid |
| 2 | idx_xkbm_ctrldimmapping |  | fid |

---

## 编制维度值-子表 t_xkbm_rptdimensionentry

- **表名称：** 编制维度值-子表
- **表名：** t_xkbm_rptdimensionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedatafield2 | 基础资料2 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 3 | fbasedatafield1 | 基础资料1 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 4 | fctrldimfiltertype | 控制维度选择方式 | varchar | 10 |  | √ | ' ' | 控制维度选择方式,枚举: 0 :选择 1 :条件 |
| 5 | fbasedatafield3 | 基础资料3 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 6 | fassistantfield3 | 辅助资料3 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 7 | fassistantfield2 | 辅助资料2 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 8 | fassistantfield1 | 辅助资料1 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | frptdimflex | 编制维度 | int8 | 64 |  | √ | 0 | [主维度组合引用 xkbm_maindimref](../xkbm_files/xkbm_maindimref.md) |
| 11 | frptdim | 编制维度值 | int8 | 64 |  | √ | 0 | null 010 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_rptdimensionentry |  | fentryid |
| 2 | idx_xkbm_rptdimensionentry |  | fid |

---

## 编制维度字段关系-子表 t_xkbm_rptdimmapping

- **表名称：** 编制维度字段关系-子表
- **表名：** t_xkbm_rptdimmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frptfieldkey | 对应字段 | varchar | 50 |  | √ | ' ' | 对应字段 |
| 3 | frptdimensionid | 编制维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_rptdimmapping |  | fentryid |
| 2 | idx_xkbm_rptdimmapping |  | fid |

---

## 控制维度字段关系-多语言表 t_xkbm_ctrldimmapping_l

- **表名称：** 控制维度字段关系-多语言表
- **表名：** t_xkbm_ctrldimmapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fctrldimname | 维度名称 | varchar | 570 |  | √ | ' ' | 维度名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_ctrldimmapping_l |  | fpkid |
| 2 | idx_xkbm_ctrldimmapping_l |  | fentryid,flocaleid |

---

## 控制维度过滤条件-子表 t_xkbm_ctrldimfilterentry

- **表名称：** 控制维度过滤条件-子表
- **表名：** t_xkbm_ctrldimfilterentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fctrlfilterasstacttype | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 2 | fctrldimensionid | 控制维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fctrldimsql | 过滤条件sql | varchar | 2000 |  | √ | ' ' | 过滤条件sql |
| 5 | fctrldimjson | 过滤条件json | varchar | 2000 |  | √ | ' ' | 过滤条件json |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_ctrldimfilterentry |  | fentryid |
| 2 | pk_xkbm_ctrldimfilterentry |  | fdetailid |

---

## 控制维度值-子表 t_xkbm_ctrldimensionentry

- **表名称：** 控制维度值-子表
- **表名：** t_xkbm_ctrldimensionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fctrlassistantfield1 | 辅助资料1 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 2 | fctrldimflex | 控制维度 | int8 | 64 |  | √ | 0 | [主维度组合引用 xkbm_maindimref](../xkbm_files/xkbm_maindimref.md) |
| 3 | fctrlassistantfield2 | 辅助资料2 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 4 | fctrlassistantfield3 | 辅助资料3 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fctrlbasedatafield1 | 基础资料1 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 8 | fctrldim | 控制维度值 | int8 | 64 |  | √ | 0 | null 010 |
| 9 | fctrlbasedatafield2 | 基础资料2 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fctrlbasedatafield3 | 基础资料3 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_ctrldimensionentry |  | fentryid |
| 2 | pk_xkbm_ctrldimensionentry |  | fdetailid |
