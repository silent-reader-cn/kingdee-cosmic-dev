# 客户物料可销控制-sm_custmatctrl

## 客户物料可销控制-主表 t_sm_custmatctrl

- **表名称：** 客户物料可销控制-主表
- **表名：** t_sm_custmatctrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fgroupid | 控制维度 | int8 | 64 |  | √ | 0 | 客户物料分组 sm_custmatctrlgrp |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 6 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 8 | fcontroltype | 控制类型 | bpchar | 1 |  | √ | ' ' | 控制类型,枚举: A :允销 B :限销 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcustomergroupid | 客户分类 | int8 | 64 |  | √ | 0 | 客户分类 bd_customergroup |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fcustomerid | 客户编码 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_custmatctrl_material |  | fmaterialid |
| 2 | pk_t_sm_custmatctrl |  | fid |

---

## 客户物料可销控制-多语言表 t_sm_custmatctrl_l

- **表名称：** 客户物料可销控制-多语言表
- **表名：** t_sm_custmatctrl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sm_custmatctrl_l |  | fpkid |
| 2 | idx_sm_custmatctrl |  | fid,flocaleid |
