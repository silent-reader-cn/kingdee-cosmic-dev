# 销售员物料可销控制-sm_salesmatctrl

## 销售员物料可销控制-多语言表 t_sm_salesmatctrl_l

- **表名称：** 销售员物料可销控制-多语言表
- **表名：** t_sm_salesmatctrl_l

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
| 1 | pk_t_sm_salesmatctrl_l |  | fpkid |
| 2 | idx_sm_salesmatctrl |  | fid,flocaleid |

---

## 销售员物料可销控制-主表 t_sm_salesmatctrl

- **表名称：** 销售员物料可销控制-主表
- **表名：** t_sm_salesmatctrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fgroupid | 控制维度 | int8 | 64 |  | √ | 0 | 销售员物料分组 sm_salesmatctrlgrp |
| 4 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 7 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 9 | fcontroltype | 控制类型 | bpchar | 1 |  | √ | ' ' | 控制类型,枚举: A :允销 B :限销 |
| 10 | fsalesid | 销售员编码 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_salesmatctrl_fid |  | fsalesid |
| 2 | pk_t_sm_salesmatctrl |  | fid |
